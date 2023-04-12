import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


def create_initial_summary(result: pd.DataFrame, index = "Twitter Handle") -> pd.io.formats.style.Styler:
    """
    This function produces a high level summary table that has the number and proportion of pos/neg sentiment for each company
    :param result: Pandas data frame with the following columns: ['Twitter Handle', 'Date', 'Prediction', 'Confidence']
    :return: stylized table
    """
    # Determing the count for each sentiment classification
    results_counts = result.drop(["Date", "Confidence"], axis=1).groupby([index, "Prediction"]).value_counts().reset_index()

    # Fixing the columns
    results_counts.columns = [index, "Prediction", "Count"]

    # Computing the total number of results for each column
    totals = result.drop(["Date", "Confidence", "Prediction"], axis=1).groupby([index]).size().reset_index()

    # Fixing the column names
    totals.columns = [index, "total"]

    # Mering the dfs together
    initial_results = pd.merge(results_counts, totals, on=index)

    # Computing the proportion for both pos and neg
    initial_results["Proportion"] = initial_results["Count"].div(initial_results["total"])

    # Removing unneccessary column
    initial_results = initial_results.drop("total", axis=1)

    # Breaking the results up so they can be pivoted
    initial_results_count = initial_results.drop("Proportion", axis=1)
    initial_results_prop = initial_results.drop("Count", axis=1)

    # Pivoting the results to get sentiment labels in columns
    counts_pivoted = pd.pivot_table(data=initial_results_count, values="Count", index=index, columns="Prediction")
    prop_pivoted = pd.pivot_table(data=initial_results_prop, values="Proportion", index=index, columns="Prediction")

    # Getting rid of axis name and resetting index
    counts_pivoted = counts_pivoted.rename_axis(None, axis=1).reset_index()
    prop_pivoted = prop_pivoted.rename_axis(None, axis=1).reset_index()

    # Mering the pivoted dfs together
    pivoted_results = pd.merge(counts_pivoted, prop_pivoted, on=index, suffixes=('_C', '_P'))

    # Setting the company as the indexcreate_timeseries_summary
    pivoted_results.set_index(index, inplace=True)

    # Defining lists to use in multi index column names
    types = ["Count", "Count", "Proportion", "Proportion"]
    sentiment = ["Negative", "Positive", "Negative", "Positive"]

    # Rounding and converting to strings
    pivoted_results = pivoted_results.round(2).astype(str)

    # Zipping the lists together
    multi_index_columns = list(zip(types, sentiment))

    # Creating the multilevel columns
    pivoted_results.columns = pd.MultiIndex.from_tuples(multi_index_columns)

    # Setting table styles
    pivoted_results = pivoted_results.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
    pivoted_results.set_properties(**{'text-align': 'center'})

    return pivoted_results


def create_initial_distribution(results: dict, index="Twitter Handle", type="Twitter"):
    """
    This function accepts a pandas df and builds a distribution plot for each company
    :param result: Pandas data frame with the following columns: ['Twitter Handle', 'Date', 'Prediction', 'Confidence']
    :param model_name: the name of the model
    :return: the matplotlib plot
    """

    # Getting list of models
    models = list(results.keys())

    # Making a copy
    results = results.copy()
    for key in results.keys():
        # Dropping the prediction
        results[key] = results[key].drop("Prediction", axis=1)

    # Setting the initial plot size
    # plt.figure(figsize=(,2)) # Plot size
    plt.style.use('seaborn-whitegrid')

    # Getting the names of companies
    companies = results[list(results.keys())[0]][index].unique()

    num_companies = len(companies)

    # Defining grid of plots
    fig, axs = plt.subplots(num_companies + 1, 2, sharex=True, gridspec_kw={"height_ratios": [0.02 if i == 0 else 1 for i in range(0, num_companies + 1)]})

    # Setting figure dimensions
    fig.set_figwidth(10)
    fig.set_figheight(10)
    fig.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.95])

    # Setting labels
    fig.supxlabel('Sentiment (Negative to Positive)')
    fig.supylabel('Frequency')
    plt.suptitle(f"Sentiment Distribution: " + r"$\bf{" + type + "}$", fontsize=14)

    # for i, ax in enumerate(axs.flatten()[2:]):
    #     ax.set_title("Title {}".format(i+1))

    # for i, ax in enumerate(axs.flatten()[:2]):
    #     ax.set_title("Columntitle {}".format(i+1), fontweight='bold')

    fontsize = 15
    axs[0, 0].set_title(f"Model: " + r"$\bf{" + models[0] + "}$", fontsize=fontsize)
    axs[0, 1].set_title(f"Model: " + r"$\bf{" + models[1] + "}$", fontsize=fontsize)
    axs[0, 0].axis("off")
    axs[0, 1].axis("off")

    # Iterating through each company
    for col_index, key in enumerate(results.keys()):
        for row_index in range(1, num_companies + 1):
            company = companies[row_index - 1]

            # Filtering the results
            filtered_result = results[key][results[key][index] == company]

            # CITATION: https://github.com/arseniyturin/Matplotlib-Histogram/blob/master/histogram.ipynb

            # Creaing the histogram
            n, bins, patches = axs[row_index, col_index].hist(filtered_result["Confidence"], bins=50, facecolor='#2ab0ff', edgecolor='#169acf', linewidth=0.5)

            n = n.astype('int')  # n should be integer, otherwise it wouldn't work properly

            # Accessing each bin, changing color according to height
            for i in range(len(patches)):
                patches[i].set_facecolor(plt.cm.viridis(n[i] / max(n)))

            # Setting labels
            # CITATION: https://stackoverflow.com/questions/34937048/make-part-of-a-matplotlib-title-bold-and-a-different-color
            axs[row_index, col_index].set_title(f"{index}: " + r"$\bf{" + company + "}$")


def create_timeseries_summary(results: dict, min_weeks: int = 10, index="Twitter Handle", type="Twitter"):
    """
    This function accepts a pandas df and builds a lineplot that vizualizes the sentiment distribution week over week
    :param result: Pandas data frame with the following columns: ['Twitter Handle', 'Date', 'Prediction', 'Confidence']
    :param min_weeks: Parameter to filter out companies with predictions that aren't over the minimum number of weeks
    :param model_name: the name of the model
    :return: the matplotlib plot
    """
    # Getting list of models
    models = list(results.keys())

    # Getting the names of comanies
    companies = results[list(results.keys())[0]][index].unique()

    # Getting number of companies
    num_companies = len(companies)

    # Setting the initial plot size
    # plt.figure(figsize=(,2)) # Plot size
    plt.style.use('seaborn-whitegrid')

    # Defining grid of plots
    fig, axs = plt.subplots(num_companies + 1, 2, gridspec_kw={"height_ratios": [0.02 if i == 0 else 1 for i in range(0, num_companies + 1)]})

    # Setting figure dimensions
    fig.set_figwidth(10)
    fig.set_figheight(12)
    fig.tight_layout(pad=4.0, rect=[0, 0.03, 1, 0.95])

    # Setting labels
    fig.supxlabel('Time by Week')
    fig.supylabel('Sentiment Proportion (Negative to Positive)')
    plt.suptitle(f"Change in Sentiment Over Time: " + r"$\bf{" + f"{type}" + "}$", fontsize=14)

    fontsize = 15
    axs[0, 0].set_title(f"Model: " + r"$\bf{" + models[0] + "}$", fontsize=fontsize)
    axs[0, 1].set_title(f"Model: " + r"$\bf{" + models[1] + "}$", fontsize=fontsize)
    axs[0, 0].axis("off")
    axs[0, 1].axis("off")

    # Iterating through each company
    for col_index, key in enumerate(results.keys()):
        for row_index in range(1, num_companies + 1):
            # Getting the company name
            company = companies[row_index - 1]

            # Filtering the results
            filtered_result = results[key][results[key][index] == company]

            grouped_by_week_pred = filtered_result.drop('Confidence', axis=1).groupby([pd.Grouper(key='Date', freq='W'), "Prediction"]).count().reset_index()

            positive = grouped_by_week_pred[grouped_by_week_pred["Prediction"] == "Positive"]
            negative = grouped_by_week_pred[grouped_by_week_pred["Prediction"] == "Negative"]

            together = pd.merge(positive, negative, on="Date", suffixes=('_P', '_N'))

            together["Prop"] = together[f"{index}_P"] / (together[f"{index}_P"] + together[f"{index}_N"])

            together["Prop_Avg"] = together["Prop"].rolling(window=4).mean()

            axs[row_index, col_index].plot(together["Date"], together["Prop"], alpha=0.3, label='Sentiment Proportion (Unsmoothed)')

            y_smooth = savgol_filter(together["Prop"], window_length=11, polyorder=2)

            # axs[row_index, col_index].plot(together["Date"], together["Prop_Avg"])
            axs[row_index, col_index].plot(together["Date"], y_smooth, label='Sentiment Proportion (Smoothed)')
            #
            # grouped_by_week_mean = filtered_result.drop(['Prediction', 'Twitter Handle'], axis=1).groupby([pd.Grouper(key='Date', freq='W')]).mean(True).reset_index()

            # axs[row_index, col_index].plot(grouped_by_week_mean["Date"], grouped_by_week_mean["Confidence"])

            # Setting the y-axis range
            axs[row_index, col_index].set_ylim(bottom=0, top=1)

            axs[row_index, col_index].legend()

            # Rotating the x-axis labels
            for tick in axs[row_index, col_index].get_xticklabels():
                tick.set_rotation(45)

            # Setting labels
            # CITATION: https://stackoverflow.com/questions/34937048/make-part-of-a-matplotlib-title-bold-and-a-different-color
            axs[row_index, col_index].set_title(f"{index}: " + r"$\bf{" + company + "}$")
    plt.legend()

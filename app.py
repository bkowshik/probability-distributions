import random

import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt


st.markdown('# Probability distributions')

st.markdown('Ref: https://en.wikipedia.org/wiki/Probability_distribution')
st.markdown('> In probability theory and statistics, a probability distribution is the mathematical function that gives the probabilities of occurrence of different possible outcomes for an experiment.')
st.markdown('---')


column_1, column_2 = st.columns([7, 3])

with column_2:
    simulations = st.slider('Simulations', min_value=10, max_value=1000, value=500, step=10)
    flips = st.slider('Flips', min_value=1, max_value=100, value=100, step=1)
    heads = st.slider('Heads (Success)', min_value=1, max_value=100, value=50, step=1)

with column_1:
    # The number of times we want to run the simulation.
    results = []
    for simulation in range(simulations):

            # The number of repeats in each simulation.
        success = []
        for i in range(simulations):

                    # The number of coin flips in each run of the simulation.
            counts = 0
            for i in range(flips):

                            # Working with a fair-coin
                toss = 'HEAD' if random.random() < 0.5 else 'TAIL'
                if toss == 'HEAD':
                    counts += 1

            if counts == heads:
                success.append(1)
            else:
                success.append(0)

        df = pd.DataFrame(success, columns=['success'])
        results.append({'simulations': simulation, 'probability': df['success'].mean()})

    results = pd.DataFrame(results)

    # Calculate the mean probability.
    probability = round(results['probability'].mean(), 4)

    # Visualize probability as a histogram.
    fig, ax = plt.subplots()
    results['probability'].plot.hist(ax=ax)
    ax.set_xlim(0, 1)
    ax.set_xlabel('Probability')
    ax.set_ylabel('Frequency')
    ax.axvline(probability, color='r', linestyle='-', linewidth=1.2)

    plt.grid(linestyle='dotted')
    st.markdown('Probability of flipping {} heads in {} flips is: `{}`'.format(heads, flips, probability))

    st.pyplot(fig)
Date: 2026-05-18

## Summary of files

`1_process_prompts.qmd` takes the the two main CSVs downloaded from Google Drive, `prompts\WVS_prompts_v4_English - Additional content.csv` and `prompts\WVS_prompts_v4_English - Questions.csv`, which are in a format that is easier for humans to edit, and processes them into a version that makes it easier for `survey.py` to read.

`survey.py` includes functions to make API calls to OpenRouter in parallel and saves data to SQL. It uses Pydantic to ensure that the data format is valid. Pydantic also makes it easy to access other types of information. 

The scripts starting with `2`, aka 2_american.py, 2_qwen,py, 2_deepseek.py are scripts for different models. They run the functions in `survey.py`. Multiple scripts make it easier to run separate processes at the same time.

To run multiple files and processes at once without feear of accidentally closing the processes, use tmux in WSL.

`3_convert.py` concatenates and converts the .db files in `data/raw` into one csv file `full_dataset.csv`

`4_data_info.qmd` provides some basic information on the collected data.

`4_clean.qmd` cleans the `full_dataset.csv` to the final version, `final_data.csv`. 

The files in `logs` are produced by using tmux with the logged filed option. These logging messages are typically just printed out in the terminal, but are saved to a file when specified when using tmux.

## Temperature

For the American models, a temperature of 2 (maximum OpenRouter temperature) worked well. However, for some of the Chinese models, a temperature of 2 produced extremely inconsistent and unreasonable results (bad formatting, numbers outside of range, thinking processes that did not make sense). It also lead to extremely slow and expensive runs, and required multiple runs to (maybe) get more proper results. Therefore, we had to lower the temperature to 1.5 for the Chinese models.
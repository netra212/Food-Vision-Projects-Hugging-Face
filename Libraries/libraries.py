# Install dependencies
try:
    import datasets, evaluate, accelerate
    import gradio as gr
except ModuleNotFoundError:
    !pip install -U datasets evaluate accelerate gradio
    import datasets, evaluate, accelerate
    import gradio as gr

import random 

import numpy as np
import pandas as pd

import torch
import transformers

print(f"Using transformers version: {transformers.__version__}")
print(f"Using torch version: {torch.__version__}")
print(f"Using datastes version: {datasets.__version__}")
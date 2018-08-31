import sys

import pandas as pd
from tqdm import tqdm
import imblearn
from sklearn.model_selection import cross_validate

from .jupyter import printmd


def get_name(o, name=None):
    if name is not None:
        return name
    try:
        return o.__name__
    except AttributeError:
        return type(o).__name__


def create_pipelines(pipeline_steps):
    def g(prefix, remaining):
        if not remaining:
            yield prefix
        else:
            name, step = remaining[0]
            for value in (step if isinstance(step, list) else [step]):
                yield from g(prefix + [(name, value)], remaining[1:])
    return list(g([], pipeline_steps))


def describe_pipeline_as_dict(pipeline):
    return {
        step_name: get_name(step)
        for step_name, step in pipeline.steps
    }


def multi_pipeline_steps_cross_validate_scores(
    pipelines, X, y, *args, cv=4, scoring=('accuracy', 'f1'), verbose=False, progress=True, **kwargs):

    printmd('X %s -> y %s' % (X.shape, y.shape))
    scores_dfs = []
    if progress:
        pipelines = tqdm(pipelines, leave=False, file=sys.stdout)
    for pipeline in pipelines:
        if isinstance(pipeline, list):
            pipeline = imblearn.pipeline.Pipeline(pipeline)
        if verbose:
            print('running pipeline: %s (X %s)' % (
                describe_pipeline_as_dict(pipeline),
                X.shape
            ))
        scores = cross_validate(
            pipeline, X, y, *args, **kwargs, cv=cv, scoring=scoring
        )
        df = pd.DataFrame({
            **{
                score: scores['test_%s' % score]
                for score in scoring
            }
        })
        for step_name, step_value in describe_pipeline_as_dict(pipeline).items():
            df[step_name] = step_value
        scores_dfs.append(df)
    return pd.concat(scores_dfs)

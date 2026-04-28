"""Shapelet based time series classifiers.

Modified to include a range of experimental shapelet based classifiers
"""




__all__ = [
    "ShapeletTransformClassifier",
    "RDSTClassifier", 
    "RUSTClassifier", #Experimental, see module docstring for details
    "RDSTClassifier_rotation_only", #Experimental, see module docstring for details
    "RDSTClassifier_rotation_pipeline",#Experimental, see module docstring for details
    "RDSTClassifier_rotation_pipeline_2",#Experimental, see module docstring for details
    "RDSTClassifier_rotation_pipeline_3",#Experimental, see module docstring for details
    "RDSTClassifier_rotation_pipeline_4",#Experimental, see module docstring for details
    "RDSTClassifier_rotation_pipeline_pca_95",#Experimental, see module docstring for details
    "RDSTClassifier_rotation_pipeline_pca_99",#Experimental, see module docstring for details
    "SASTClassifier",
    "RSASTClassifier",
    "LearningShapeletClassifier",
    "BatchRDSTClassifier",#Experimental, see module docstring for details
    "PruneBatchRDSTClassifier",#Experimental, see module docstring for details
    "EarlyBatchRDSTClassifier",#Experimental, see module docstring for details
]

from aeon.classification.shapelet_based._ls import LearningShapeletClassifier
from aeon.classification.shapelet_based._rdst_batch_early import EarlyBatchRDSTClassifier
from aeon.classification.shapelet_based._rdst_batch_prune import PruneBatchRDSTClassifier
from aeon.classification.shapelet_based._rdst_batch import BatchRDSTClassifier
from aeon.classification.shapelet_based._rdst import RDSTClassifier
from aeon.classification.shapelet_based._rsast import RSASTClassifier
from aeon.classification.shapelet_based.rust import RUSTClassifier
from aeon.classification.shapelet_based._sast import SASTClassifier
from aeon.classification.shapelet_based._rdst_rotation_pipeline import RDSTClassifier_rotation_pipeline
from aeon.classification.shapelet_based._rdst_rotation_pipeline_2 import RDSTClassifier_rotation_pipeline_2
from aeon.classification.shapelet_based._rdst_rotation_pipeline_3 import RDSTClassifier_rotation_pipeline_3
from aeon.classification.shapelet_based._rdst_rotation_pipeline_4 import RDSTClassifier_rotation_pipeline_4
from aeon.classification.shapelet_based._rdst_rotation_pipeline_pca_95 import RDSTClassifier_rotation_pipeline_pca_95
from aeon.classification.shapelet_based._rdst_rotation_pipeline_pca_99 import RDSTClassifier_rotation_pipeline_pca_99
from aeon.classification.shapelet_based._rdst_rotation_only import RDSTClassifier_rotation_only
from aeon.classification.shapelet_based._stc import ShapeletTransformClassifier

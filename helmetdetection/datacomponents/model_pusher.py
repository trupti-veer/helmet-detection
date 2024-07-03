import os
import sys
import torch
import math
import pandas as pd
import numpy as np
from tqdm import tqdm
from torch.utils.data import DataLoader
from helmetdetection.constants import *
from helmetdetection.logger import logging
from helmetdetection.exception import HDException
from helmetdetection.utils.main_utils import load_object
from helmetdetection.entity.config_entity import ModelPusherConfig
from helmetdetection.configuration.s3_operations import S3Operation
from helmetdetection.entity.artifacts_entity import ModelPusherArtifacts

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig, s3: S3Operation):

        self.model_pusher_config = model_pusher_config
        self.s3 = s3

    def initiate_model_pusher(self) -> ModelPusherArtifacts:
        """
            Method Name :   initiate_model_pusher
            Description :   This method initiates model pusher.

            Output      :    Model pusher artifact
        """
        logging.info("Entered initiate_model_pusher method of ModelTrainer class")
        try:
            # Uploading the model to s3 bucket
            self.s3.upload_file(
                self.model_pusher_config.BEST_MODEL_PATH,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")

            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifacts(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH,
            )
            logging.info("Exited the initiate_model_pusher method of ModelTrainer class")
            return model_pusher_artifact

        except Exception as e:
            raise HDException(e, sys) from e

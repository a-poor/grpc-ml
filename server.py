import sys
import pickle
import logging
from concurrent.futures import ThreadPoolExecutor

import grpc

from protos import app_pb2
from protos import app_pb2_grpc


PORT = "50051"
MODEL_PATH = "./data/model.pkl"

class PredictorService(app_pb2_grpc.PredictorServicer):
    def Predict(self, request, context):
        # Load the model
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)

        # Read in the data

        # Make the prediction

        # Format the result

        # Return the result
        return app_pb2.PredictResponse(
            success=True,
        )

def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=5))

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    serve()
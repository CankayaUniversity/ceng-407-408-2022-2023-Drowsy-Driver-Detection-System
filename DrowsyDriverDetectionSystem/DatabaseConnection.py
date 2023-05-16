from  CaptureandDetect import detect
from StartDetection import gen_frames
from pymongo import MongoClient
import bcrypt
import pymongo
# Connect to your Mongo DB database
def MongoDB():

    client = pymongo.MongoClient("mongodb+srv://admin:ikizler2000@cluster0.dlat3qm.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    records = db.register
    #records.comments.insert_one(comment_doc)
    return records
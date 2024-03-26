from modelHelper import ModelHelper

test = ModelHelper()
tracks_returned = test.makePredictions('The Hills', 'The Weeknd')
print(tracks_returned)
'''You have been tasked with identifying the most popular NFT creators in your collection. 
A creator is considered "popular" if they have created more than one NFT in the collection.
Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.
Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.'''

def identify_popular_creators(nft_collection):
    creater_count = {}

    for nft in nft_collection:
        creator = nft["creator"]
        if creator not in creater_count:
            creater_count[creator] = 0
        creater_count[creator] = creater_count[creator] + 1

    popular_creators = []

    for creator, count in creater_count.items():
        if count > 1:
            popular_creators.append(creator)

    return popular_creators



nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
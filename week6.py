# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next
        
# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# # Function with a bug!
# def remove_song(playlist_head, song):
#     if not playlist_head:
#         return None
#     if playlist_head.song == song:
#         return playlist_head.next

#     current = playlist_head
#     # print(current.next.song)
#     while current.next:
#         if current.next.song == song:
#             current.next = current.next.next  # Change the pointer not the node itself
#             return playlist_head 
#         current = current.next

#     return playlist_head

# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
    if not song_audio or not song_audio.next or not song_audio.next.next:
        return 0

    critical_points = 0

    prev = song_audio
    curr = song_audio.next
    next_node = song_audio.next.next

    while next_node:
        if curr.value > prev.value and curr.value > next_node.value:
            critical_points += 1
        elif curr.value < prev.value and curr.value < next_node.value:
            critical_points += 1

        prev = curr
        curr = next_node
        next_node = next_node.next

    return critical_points


song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))
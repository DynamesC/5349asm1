#!/usr/bin/python3

import sys
# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE,SIG_DFL)

def tag_mapper():
    """ This mapper select tags and return the tag-owner information.
    Input format: video_id,trending_date,category_id,category,publish_time
    ,views,likes,dislikes,comment_count,ratings_disabled,video_error_or_removed,country
    """

    for line in sys.stdin:
        # Clean input and split it
        parts = line.strip().split(",")

        # Check that the line is of the correct format
        # If line is malformed, we ignore the line and continue to the next line
        if len(parts) != 12 or parts[0] == "video_id":
            continue

        video_id = parts[0]
        category = parts[3]
        country = parts[11]

            # In hadoop streaming, the output is sys.stdout, thus the print command
        print("{}\t{}|{}".format(category, video_id, country))

if __name__ == "__main__":
    tag_mapper()

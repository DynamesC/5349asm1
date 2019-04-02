#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)


def tag_reducer():

    current_cat = ""
    current_id_country_dict = {}
    file = open("test", "r")

    for category, message in read_map_output(file):
        message_parts = message.split("|",1)
        video_id = message_parts[0]
        country = message_parts[1]

        if (current_cat != category) and current_cat != "":

            vals = []

            for id in current_id_country_dict:
                num_countries = len(current_id_country_dict[id])
                vals.append(num_countries)

            average = sum(vals)*1.0/len(vals)
            print("{}: {:.2f}".format(current_cat, average))

        if (current_cat != category):
            current_cat = category
            current_id_country_dict = {}

        if video_id in current_id_country_dict:
            counrty_list = current_id_country_dict[video_id]

            if country not in counrty_list:
                counrty_list.append(country)

        if video_id not in current_id_country_dict:
            current_id_country_dict[video_id] = [country]

    vals = []

    for id in current_id_country_dict:
        num_countries = len(current_id_country_dict[id])
        vals.append(num_countries)

    average = sum(vals)*1.0/len(vals)
    print("{}: {:.2f}".format(current_cat, average))
    #     # Check if the tag read is the same as the tag currently being processed
    #     if current_tag != tag:
    #
    #         # If this is the first line (indicated by the fact that current_tag will have the default value of "",
    #         # we do not need to output tag-owner count yet
    #         if current_tag != "":
    #             output = current_tag + "\t"
    #
    #             for own, count in owner_count.items():
    #                 output += "{}={}, ".format(own, count)
    #             print(output.strip())
    #
    #         # Reset the tag being processed and clear the owner_count dictionary for the new tag
    #         current_tag = tag
    #         owner_count = {}
    #
    #     owner_count[owner] = owner_count.get(owner, 0) + 1
    #
    # # We need to output tag-owner count for the last tag. However, we only want to do this if the for loop is called.
    # if current_tag != "":
    #     output = current_tag + "\t"
    #     for owner, count in owner_count.items():
    #         output += "{}={}, ".format(owner, count)
    #     print(output.strip())


if __name__ == "__main__":
    tag_reducer()

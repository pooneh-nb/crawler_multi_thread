# This is a sample crawler. It will go through the website and collect all the links

import os

#Each website you crawl is a seprate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project '+ directory)
        os.makedirs(directory)

# create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'  #  the list of sites waiting to be crawled
    crawled = project_name + '/crawled.txt' # the list of crawled sites
    if not os.path.isfile(queue):   #if project_name + 'queue.txt' does not exist, just create it
        write_file(queue, base_url) # start point
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close

# Add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:   #a: append mode, at the end of the file
        file.write(data + '\n')

# Delete the content of a file
def delete_file_contents(path):
    with open(path, 'w'):
       pass         #keyword to say do nothing!

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
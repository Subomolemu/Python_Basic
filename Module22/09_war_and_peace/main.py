import collections
import zipfile


def unzip(archive):
	z_file = zipfile.ZipFile(archive, 'r')
	for i_file_name in z_file.namelist():
		z_file.extract(i_file_name)
		

def collect_stats(file_name):
	result = {}
	if file_name.endswith('.zip'):
		unzip(file_name)
		file_name = ''.join((file_name[:-3], 'txt'))
	text_file = open(file_name, 'r', encoding='utf-8')
	for i_line in text_file:
		for j_char in i_line:
			if j_char.isalpha():
				if j_char not in result:
					result[j_char] = 0
				result[j_char] += 1
	text_file.close()
	
	return result


def print_stats(stats):
	print("+{:-^19}+".format('+'))
	print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
	print("+{:-^19}+".format('+'))
	for char, count in stats.items():
		print("|{: ^9}|{: ^9}|".format(char, count))
	print("+{:-^19}+".format('+'))


def sort_by_frequency(stats_dict):
	sorted_values = sorted(stats_dict.values(), reverse=True)
	sorted_dict = collections.OrderedDict()
	for i_value in sorted_values:
		for j_key in stats_dict.keys():
			if stats_dict[j_key] == i_value:
				sorted_dict[j_key] = stats_dict[j_key]
				
	return sorted_dict
	
	
file = 'voyna-i-mir.zip'
statistics = collect_stats(file)
statistics = sort_by_frequency(statistics)
print_stats(statistics)

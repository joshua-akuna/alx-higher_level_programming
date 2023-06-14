#include "Python.h"
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - print some basic information
 *	about a bytes object
 * @p: bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *) p;
	int size;
	char *val;
	
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	
	size = PyBytes_Size(p);
	val = bytes->ob_sval;

	printf("  size: %d\n  trying string: %s\n", size, bytes->ob_sval);
	size++;
	
	if (size > 10)
		size = 10;
	printf("  first %d bytes:", size);
	
	while (size--)
		printf(" %.2x", (unsigned char) *val++);
	printf("\n");
}

/**
 * print_python_list - prints some basic information
 *	about a python list
 * @p: list to print information about
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	long long count = -1, size;
	const char *type;
	
	printf("[*] Python list info\n");
	size = (long long) PyList_Size(p);
	
	printf("[*] Size of the Python List = %lld\n", size);
	printf("[*] Allocated = %lld\n", (long long) list->allocated);
	
	while (++count < size)
	{
		type = list->ob_item[count]->ob_type->tp_name;
		printf("Element %lld: %s\n", count, type);
		
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[count]);
	}
}

#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print some basic information about
 *	Python bytes objects
 * @p: a pointer argument of type PyObject.
 */
void print_python_bytes(PyObject *p)
{
	/* PyBytesObject *bytes = (PyBytesObject *)p;*/
	Py_ssize_t size, i; 
	char *str;
	
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", size + 1);

	for (i = 0; i <= size; i++)
		printf(" %02x", (unsigned char)str[i]);
	putchar('\n');
}

/**
 * print_python_list - Print some basic information
 *	about Python lists
 * @p: a pointer argument of type PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i, allocated;
	PyObject *item;
	
	size = PyList_Size(p);
	allocated = list->allocated;
	
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}


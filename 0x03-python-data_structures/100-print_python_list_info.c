#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info
 *	about Python lists.
 * @p: an pointer argument of type PyObject.
 */


void print_python_list_info(PyObject *p) {
	Py_ssize_t size, allocated, i;
	PyListObject *list = (PyListObject *)p;
	const char *typeName;
	PyObject *element;

	size = PyList_Size(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	
	for (i = 0; i < size; i++) {
		element = PyList_GetItem(p, i);
		typeName = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", i, typeName);
	}
}


#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info
 *	about Python lists.
 * @p: an pointer argument of type PyObject.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t allocated = list->allocated, size = PyList_Size(p), i;
	PyObject *item;
	const char *type_name;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated  = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		*type_name = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i. type_name);
	}
}

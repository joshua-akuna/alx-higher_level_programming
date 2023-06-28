#include <Python.h>

/**
 * print_python_bytes - prints some basic information
 *	about Python byte objects.
 * @p: a pointer to a Python List Object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbo = (PyBytesObject *)p;
	PyVarObject *pvo = NULL;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	pvo = (PyVarObject *)p;
	size = pvo->ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", pbo->ob_sval);

	if (pvo->ob_size >= 10)
		size = 10;
	else
		size++;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", pbo->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - prints some basic information
 *	about Python float objects.
 * @p: a pointer to a Python List Object.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *pfo = (PyFloatObject *)p;
	char *ptr = NULL;

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	ptr = PyOS_double_to_string(pfo->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", ptr);
	PyMem_Free(ptr);
}

/**
 * print_python_list - prints some basic information
 *	about Python list objects.
 * @p: a pointer to a Python List Object.
 */
void print_python_list(PyObject *p)
{
	PyListObject *plo = (PyListObject *)p;
	PyVarObject *pvo = NULL;
	Py_ssize_t size, allocated, count = 0;
	const char *type;

	pvo = (PyVarObject *)p;
	size = pvo->ob_size;
	allocated = plo->allocated;

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	while (count < size)
	{
		type = plo->ob_item[count]->ob_type->tp_name;
		printf("Element %ld: %s\n", count, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(plo->ob_item[count]);
		else if (!strcmp(type, "float"))
			print_python_float(plo->ob_item[count]);
		count++;
	}
}

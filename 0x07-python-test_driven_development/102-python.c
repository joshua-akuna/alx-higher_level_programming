#include "Python.h"
#include <stdio.h>
#include <locale.h>

/**
 * print_python_string - the function prints Python strings.
 * *p: a pointer to a valid/invalid python string.
 */
void print_python_string(PyObject *p)
{
	PyASCIIObject *pao = (PyASCIIObject *) p;
	wchar_t *ptr;
	Py_ssize_t size;
	
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	
	setlocale(LC_ALL, "");
	if (pao->state.ascii == 1)
	{
		printf("  type: compact ascii\n");
		printf("  length: %lld\n", (long long) pao->length);
		printf("  value: %s\n", (char *) (pao + 1));
	}
	else if (pao->state.compact == 1)
	{
		printf("  type: compact unicode object\n");
		printf("  length: %lld\n", (long long) pao->length);
		ptr = PyUnicode_AsWideCharString(p, &size);
		printf("  value: %ls\n", ptr);
		PyMem_Free(ptr);
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}

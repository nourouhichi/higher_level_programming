#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list - prints some info
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, j = 0;
	PyObject *list;

	i = (((PyVarObject *)(p))->ob_size);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", i);
	printf("[*] Allocated = %lu\n", (((PyListObject *)(p))->allocated));

	while (j < i)
	{
		list = (((PyListObject *)(p))->ob_item[j]);
		printf("Element %lu: %s\n", j, (char *)list->ob_type->tp_name);
		j++;

	}
}
/**
 *print_python_bytes - prints bytes
 *@p: python object
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		exit(0);
	}

}

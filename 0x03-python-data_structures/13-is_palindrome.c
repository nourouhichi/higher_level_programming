#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks is a list is a palin
 * @head: pointer to the head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int i, j;
	listint_t *road_runner = *head;
	int array[1024];

	if (!*head)
		return (1);
	for (i = 0; road_runner != NULL; i++)
	{
		array[i] = road_runner->n;
		road_runner = road_runner->next; }
	if (i % 2 != 0)
		return (0);
	for (i--, j = 0; i > j ; i--, j++)
	{
		if (array[i] != array[j])
			return (0);
	}
	return (1);
}


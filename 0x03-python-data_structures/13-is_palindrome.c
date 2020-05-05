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
	int *array;

	if (!head)
		return (0);
	if (!*head || !(*head)->next)
		return (1);
	array = malloc(sizeof(int) * 100);
	for (i = 0; road_runner; i++)
	{
		array[i] = road_runner->n;
		road_runner = road_runner->next; 
	}
	for (i--, j = 0; i >= j ; i--, j++)
	{
		if (array[i] != array[j])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}


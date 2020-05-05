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
	listint_t *runner = *head;
	int i, j, array[1024], x = 0;

	if (!head || !*head || !(*head)->next)
		return (1);
	for (i = 0; runner && x < 1024; i++, runner = runner->next, x++)
		array[i] = runner->n;
	x--;
	for (i--, j = 0; j <= x / 2 ; i--, j++)
	{
		if (array[i] != array[j])
			return (0);
	}
	return (1);
}


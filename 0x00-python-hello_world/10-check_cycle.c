#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * been_seen - checks if a pointer is in the list
 * @seen: list of pointers that have been seen
 * @list: pointer to be checked
 *
 * Return: 1 if list has been seen, 0 otherwise.
 */
int been_seen(listint_t **seen, listint_t *list)
{
	int i = 0;

	while (seen[i])
	{
		if (seen[i] == list)
			return (1);
		i++;
	}
	return (0);
}
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t **seen;
	int num_seen = 1;

	seen = malloc(sizeof(*seen) * 2);
	seen[0] = list;
	seen[1] = NULL;

	while (list)
	{
		if (num_seen > 1)
		{
			seen = realloc(seen, sizeof(*seen) * (num_seen + 1));
			if (been_seen(seen, list))
			{
				free(seen);
				return (1);
			}
			seen[num_seen - 1] = list;
			seen[num_seen] = NULL;
		}
		list = list->next;
		num_seen++;
	}

	free(seen);
	return (0);
}

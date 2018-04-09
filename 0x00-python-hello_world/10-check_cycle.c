#include "lists.h"

/**
 * _realloc - reallocates a memory block using malloc and free
 * @ptr: original pointer
 * @old_size: original size of the memory
 * @new_size: the size of the new memory block
 *
 * The contents will be copied to the newly allocated space, in the range
 * from the start of ptr up to the minimum of the old and new sizes.
 * If new_size > old_size, the “added” memory should not be initialized.
 * If new_size == old_size do not do anything and return ptr.
 * If ptr is NULL, then the call is equivalent to malloc(new_size).
 * If new_size is equal to zero, and ptr is not NULL, then the call is
 * equivalent to free(ptr). Return NULL.
 *
 * Return: a pointer to the allocated memory
 */
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	char *p;
	char *ptrc;
	unsigned int iter, i;

	if (ptr == NULL)
	{
		p = malloc(new_size);
		if (p == NULL)
			return (NULL);
		return (p);
	}

	if (new_size == 0)
	{
		free(ptr);
		return (NULL);
	}

	if (new_size == old_size)
		return (ptr);

	ptrc = ptr;
	iter = old_size > new_size ? new_size : old_size;
	p = malloc(new_size);
	if (p == NULL)
	{
		/* free(ptr); */
		return (NULL);
	}

	for (i = 0; i < iter; i++)
		p[i] = ptrc[i];
	free(ptr);
	return (p);
}

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
			seen = _realloc(seen, sizeof(*seen) * num_seen, sizeof(*seen) * (num_seen + 1));
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

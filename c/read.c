#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define FILE_SIZE_MAX 10240

static void usage(const char *name)
{
    printf("Usage: %s <file>\n", name);
}

int main(int argc, char **argv)
{
    int fd;
    int len;
    char *buf;

    if (argc != 2) {
        usage(argv[0]);
        exit(1);
    }

    if (NULL == (buf = (char *)calloc(1, FILE_SIZE_MAX))) {
        printf("Failed to calloc, max size was %d\n", FILE_SIZE_MAX);
        exit(1);
    }

    if (-1 == (fd = open(argv[1], O_RDONLY))) {
        printf("Failed to open file %s (%s)\n", argv[1], strerror(errno));
        free(buf);
        exit(1);
    }

    len = 0;
    while (0 != (len = read(fd, buf, 1023))) {
        if (-1 == len) {
            printf("Failed to read file %s (%s)\n", argv[1], strerror(errno));
            close(fd);
            free(buf);
            exit(1);
        }
        buf[len] = '\0';
        printf("%s", buf);
    }

    close(fd);
    free(buf);
    exit(0);
}

/* EOF */

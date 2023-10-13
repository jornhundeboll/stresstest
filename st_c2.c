#include <stdlib.h>
#include <stdio.h>


int main() {
    // Replace this command with your desired stress test command
    const char* stress_command = "stress --cpu 2 --io 1 --vm 1 --vm-bytes 128M --timeout 60s";

    int result = system(stress_command);

    if (result == -1) {
        // Failed to run the stress command
        perror("system");
        return 1;
    } else {
        if (WIFEXITED(result)) {
            int exit_status = WEXITSTATUS(result);
            printf("Stress test completed with exit status: %d\n", exit_status);
        } else {
            printf("Stress test did not exit normally\n");
        }
    }

    return 0;
}

# Exercise 8: Creating a Hello World Jenkins Job

## Aim
To create a Freestyle job in Jenkins that executes a shell script and displays its output in the console.

## Tools Required
- Jenkins
- Git and GitHub
- Ubuntu terminal
- Web browser

## Procedure

### Step 1: Create the Shell Script
Create `hello-world.sh` with the following code:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

Make the script executable using `chmod +x hello-world.sh`.

### Step 2: Push the Files to GitHub
Add the script and this README to the existing `kubernetes-hands-on` repository. Push them to the `main` branch.

### Step 3: Open Jenkins
Open `http://localhost:8080` and log in.

### Step 4: Create a New Job
1. Click **New Item**.
2. Enter `HelloWorld` as the job name.
3. Select **Freestyle project**.
4. Click **OK**.

### Step 5: Configure Source Code Management
1. Select **Git**.
2. Enter the URL of your `kubernetes-hands-on` GitHub repository.
3. Set the branch to `*/main`.

### Step 6: Configure the Build Step
1. Under **Build Steps**, click **Add build step → Execute shell**.
2. Enter the following command:

```bash
bash Exercise-8/hello-world.sh
```

3. Click **Save**.

### Step 7: Execute the Job
Click **Build Now**. Open the build number and select **Console Output**.

## Expected Output

```text
Hello, Jenkins!
Finished: SUCCESS
```

## Result
Successfully created and executed a Jenkins Freestyle job that runs a shell script and displays the expected output.

## Conclusion
This exercise demonstrates how Jenkins checks out source code, executes shell commands, and displays build results.

## References
- https://www.jenkins.io/doc/
- https://git-scm.com/docs

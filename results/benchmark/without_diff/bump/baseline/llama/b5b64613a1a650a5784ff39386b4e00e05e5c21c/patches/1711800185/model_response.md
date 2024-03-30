```
        private void checkInputs(ArtifactoryServer server) throws IOException {
            if (isAllBlank(server.getUrl(), step.url)) {
                throw new IOException("Server URL is missing");
            }
            if (!isBlank(step.credentialsId) && !isBlank(step.username)) {
                throw new IOException("'rtServer' step can't include both credentialsId and username");
            }

            if (!isBlank(step.credentialsId) && !isBlank(step.password)) {
                throw new IOException("'rtServer' step can't include both credentialsId and password");
            }
        }
```

The error message indicates that the symbol 'isNotBlank' cannot be found. To fix this, we can replace all instances of 'isNotBlank' with '!isBlank'. The 'isBlank' method is defined in the Java Library, so we can use it instead of 'isNotBlank' which is not defined.

Also, we can remove the 'Override' decorator as it's not needed since the method is not overriding any method in the new version.

It's important to note that the rest of the code remains the same, only the 'isNotBlank' methods have been replaced with '!isBlank' and the 'Override' decorator has been removed.
```java
  @Test
    void shouldPullPushedByTag() throws Exception {
        this.client.run("push", this.image.remote());
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", this.image.remote());
        final String output = this.client.run("pull", this.image.remote());
        
        // Check if the output contains the expected message
        if (output.contains(String.format("Status: Downloaded newer image for %s", this.image.remote()))) {
            // Success
        } else {
            // Failure
            fail("Image pull failed: " + output);
        }
    }
```
```java
  @Test
    void shouldPullPushedByDigest() throws Exception {
        this.client.run("push", this.image.remote());
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", this.image.remote());
        final String output = this.client.run("pull", this.image.remoteByDigest());
        Assert.assertTrue(
                String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest()),
                output.contains(String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest()))
        );
    }
```
```java
@Test
    void shouldPullPushedByDigest() throws Exception {
        this.client.run("push", this.image.remote());
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", this.image.remote());
        final String output = this.client.run("pull", this.image.remoteByDigest());
        String expectedOutput = String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest());
        assertThat(output, containsString(expectedOutput));
    }
```
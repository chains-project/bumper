```java
  @Test
    void shouldPullPushedByDigest() throws Exception {
        this.client.run("push", this.image.remote());
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", this.image.remote());
        String output = this.client.run("pull", this.image.remoteByDigest());
        if (output.contains("Status: Downloaded newer image for " + this.image.remoteByDigest())) {
            MatcherAssert.assertThat(output, new StringContains(false, "Status: Downloaded newer image for " + this.image.remoteByDigest()));
        } else {
            MatcherAssert.assertThat(output, new StringContains(false, "Status: Image is up to date for " + this.image.remoteByDigest()));
        }
    }
```
```java
    @Test
    void shouldPullPushedByDigest() throws Exception {
        this.client.run("push", this.image.remote());
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", this.image.remote());
        StringContains stringContains = new StringContains(String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest()));
        final String output = this.client.run("pull", this.image.remoteByDigest());
        MatcherAssert.assertThat(
                output,
                stringContains
        );
    }
```
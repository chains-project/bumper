```java
    @Test
    void largeImagePullWorks() throws Exception {
        final StringContains stringContains = new StringContains(String.format("Status: Downloaded newer image for %s", this.remote()));
        try {
            this.buildImage();
            this.client.run("push", this.remote());
            this.client.run("image", "rm", this.remote());
            final String output = this.client.run("pull", this.remote());
            MatcherAssert.assertThat(output, stringContains);
        } finally {
            this.client.run("rmi", this.remote());
        }
    }
```
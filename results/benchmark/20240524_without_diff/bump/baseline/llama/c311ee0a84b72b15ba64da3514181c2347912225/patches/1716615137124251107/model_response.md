```java
@Test
void largeImagePullWorks() throws Exception {
    try {
        this.buildImage();
        this.client.run("push", this.remote());
        this.client.run("image", "rm", this.remote());
        final String output = this.client.run("pull", this.remote());
        String expectedOutput = String.format("Status: Downloaded newer image for %s", this.remote());
        MatcherAssert.assertThat(output, Matchers.containsString(expectedOutput));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```
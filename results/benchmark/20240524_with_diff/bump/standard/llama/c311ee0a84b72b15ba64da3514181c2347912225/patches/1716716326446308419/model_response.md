```java
@org.junit.jupiter.api.Test
void largeImagePullWorks() throws java.lang.Exception {
    try {
        this.buildImage();
        this.client.run("push", this.remote());
        this.client.run("image", "rm", this.remote());
        final java.lang.String output = this.client.run("pull", this.remote());
        org.hamcrest.MatcherAssert.assertThat(output, org.hamcrest.core.StringMatchers.containsString(java.lang.String.format("Status: Downloaded newer image for %s", this.remote())));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```
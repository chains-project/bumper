```java
@org.junit.jupiter.api.Test
void shouldPullPushedByDigest() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remoteByDigest());
    org.hamcrest.MatcherAssert.assertThat(output, org.hamcrest.CoreMatchers.containsString(java.lang.String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest())));
}
```
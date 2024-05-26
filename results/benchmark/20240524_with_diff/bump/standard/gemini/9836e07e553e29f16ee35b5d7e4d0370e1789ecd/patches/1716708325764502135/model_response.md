```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.util.List<java.lang.String> output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output.get(0), new org.hamcrest.core.StringContains(false, java.lang.String.format("latest: digest: %s", original.digest())));
}
```
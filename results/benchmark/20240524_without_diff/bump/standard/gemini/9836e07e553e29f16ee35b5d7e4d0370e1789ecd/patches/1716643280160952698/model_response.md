```java
final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    org.hamcrest.MatcherAssert.assertThat(output, org.hamcrest.Matchers.not(org.hamcrest.Matchers.containsString(java.lang.String.format("Status: Downloaded newer image for %s", image))));
```
```java
final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
final java.lang.String image = this.copy(original);
final java.lang.String output = this.cli.run("push", image);
org.hamcrest.MatcherAssert.assertThat(output, org.hamcrest.Matchers.containsString(java.lang.String.format("latest: digest: %s", original.digest())));
```
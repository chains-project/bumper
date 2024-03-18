```java
@Test
void largeImageUploadWorks() throws Exception {
    try {
        this.buildImage();
        final String output = this.client.run("push", this.remote());
        MatcherAssert.assertThat(output, containsString("Pushed"));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```
In this patch, I replaced the `new StringContains(false, "Pushed")` with `containsString("Pushed")`. The `containsString` is a static method in the `org.hamcrest.CoreMatchers` class which can be statically imported. It creates a matcher that matches if the examined `String` contains the specified `String` anywhere.
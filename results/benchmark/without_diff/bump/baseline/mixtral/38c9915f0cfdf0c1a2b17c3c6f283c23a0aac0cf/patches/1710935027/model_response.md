I see that the issue is caused by the import statement of the class `Joined` from the library `org.cactoos.text`. It seems like the class `Joined` is no longer available in the latest version of the library, or there is a problem with the version used in the project.

To fix this issue, we can replace the usage of `Joined` class with an equivalent class or method from the same library or from a different library. In this case, let's use the `String.join()` method which is available in Java 8 and later versions.

Here's the fixed version of the code:
```java
import java.util.stream.Collectors;

@Override
public String income(String id, List<String> hashes) throws IOException {
    String path = String.format("/wallets/%s/income", id);
    try (HttpResponse<String> response = http.postForm(api, path,
        new Form().add("hashes", String.join(",", hashes))
    )) {
        if (response.statusCode() != 200) throw new HttpException(response.statusCode());
    }
    return response.body();
}
```
In this version, we use the `String.join()` method to concatenate the `hashes` list into a comma-separated string. This method is available in Java 8 and later versions, so it should work for most modern Java projects.

Note that this solution assumes that the Java version used in the project is 8 or later. If not, you may need to find an equivalent method in a third-party library or implement your own solution.
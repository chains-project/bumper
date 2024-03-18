It seems like the MavenProject package is not being recognized by the compiler. This could be due to a missing or incorrect version of the Maven dependency in your pom.xml file. 

You should ensure that you have the correct Maven dependency in your pom.xml file. If it's missing, add it. If it's present, try updating to the latest version.

Here is the dependency you need to add/update in your pom.xml:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.maven</groupId>
        <artifactId>maven-core</artifactId>
        <version>3.6.3</version>
    </dependency>
</dependencies>
```

After updating your pom.xml, try to rebuild your project. If the error still persists, it might be due to a problem with your IDE or build tool caching the old dependencies. In that case, you may need to re-import your Maven dependencies or clear your build tool's cache.

Please note that this is not a code change but a configuration change. Since the problem is due to a missing dependency, it cannot be fixed by modifying the Java code alone.
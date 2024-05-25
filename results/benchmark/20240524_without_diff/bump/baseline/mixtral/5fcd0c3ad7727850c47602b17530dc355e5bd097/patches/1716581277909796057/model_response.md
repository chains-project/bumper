Here's a possible patch to fix the issue:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    if (classInfo == null) {
      // Handle the case when classInfo is null
      // You can add proper error handling here
      return null;
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```

The patch checks if `classInfo` is null and handles it accordingly. This way, if the `getClassInfo` method returns null, the method won't fail and will return null instead.

Please note that you need to add proper error handling for the case when `classInfo` is null. The example above just returns null, but you should replace it with a proper error handling strategy for your use case.
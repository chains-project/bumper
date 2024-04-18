Here is a proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<String> classNames = Collections.singleton(data.getMutatedClass());
    CoverageDatabase.MutationCoverageMap classInfo = coverage.getClassInfo(classNames);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo.get(data.getMutatedClass()));
  }
```

In this patch, I created a new variable `classNames` to store the mutated class name as a set, since `getClassInfo` method expects a set of class names. Then, I used the `getClassInfo` method to get a map of mutation coverage information for the given class names. Finally, I used the map to get the mutation coverage information for the mutated class and passed it to the `MutationTestSummaryData` constructor.
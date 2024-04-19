Here is a possible patch for the failing code:
```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    Collection<ClassInfo> classInfos = coverage.getClassInfo(singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfos.stream()
        .map(classInfo -> ClassInfoVisitor.getClassInfo(classInfo.getName(), classInfo.getRawClass(), classInfo.getNumberOfMethods()))
        .collect(Collectors.toList()));
}

private <T> Set<T> singleton(T element) {
    return new HashSet<>(Collections.singletonList(element));
}
```
Explanation:

* The `getClassInfo` method of `CoverageDatabase` has been removed, so we need to find an alternative way to get the class information.
* We can use the new `getClassInfo` method of `ClassInfoVisitor` to create the class information from the `ClassInfo` objects returned by `getClassInfo`.
* We need to convert the `Collection<ClassInfo>` returned by `getClassInfo` to a `Set<ClassName>` expected by `getClassInfo`.
* We can create a helper method `singleton` to create a singleton set from an element.
* We need to extract the `name`, `rawClass`, and `numberOfMethods` from each `ClassInfo` object and pass them to `getClassInfo` method.
* We can use `stream` and `map` to transform the `Collection<ClassInfo>` to a `List<ClassInfoBuilder>`.
* We can use `collect` to convert the `List<ClassInfoBuilder>` to a `List<ClassInfo>`.
* Finally, we can create the `MutationTestSummaryData` object with the new `List<ClassInfo>`.
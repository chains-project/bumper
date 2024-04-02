Here's a possible patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // we create a new ClassInfo instance using the ClassName and the byte[] that represents the class file
    org.pitest.classinfo.ClassInfo classInfo = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass().getName(), data.getMutatedClass().getBytes()).build();
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(Collections.singleton(classInfo)));
}
```
This patch creates a new `ClassInfo` instance using the `ClassInfoBuilder` method `getClassInfo(ClassName, byte[])`, which is a new method added in the updated library version. This allows us to avoid using the removed `getClassInfo(Collection)` method.

Note that we're using the `ClassName` and `byte[]` representations of the class file, which are the same inputs used by the `ClassInfoBuilder` constructor. This ensures that we're creating a `ClassInfo` instance that accurately represents the class file.
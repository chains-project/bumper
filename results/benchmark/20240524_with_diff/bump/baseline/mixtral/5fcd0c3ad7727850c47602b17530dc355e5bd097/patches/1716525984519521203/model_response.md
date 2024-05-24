Here's a possible patch for the given client code:

```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Collection<ClassInfo> classInfos = new ArrayList<>();
    for (ClassName className : Collections.singleton(data.getMutatedClass())) {
      classInfos.add(ClassInfoVisitor.getClassInfo(className, new byte[0], 0));
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfos);
  }
```

In this patch, we iterate over the set of class names returned by `data.getMutatedClass()`, and for each class name, we create a `ClassInfo` object using the new `ClassInfoVisitor.getClassInfo()` method. We then add this `ClassInfo` object to a list, which we use to instantiate the `MutationTestSummaryData` object.

Note that we initialize the byte array and long value in `ClassInfoVisitor.getClassInfo()` with dummy values, since they are not used in the new method signature.
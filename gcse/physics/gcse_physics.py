import os
os.system('clear')

print 'Welcome to this GCSE Physics helper, with this app, you will finally be able to ace that exam!!'
print '----------------------'
print '----------------------'
step = raw_input('The first topic on this file is "The Scientific Process", would you like to learn this? (y/n) -> ')
while step != 'y' and step != 'n':
    print ' y / n '
    step = raw_input('The first topic on this file is "The Scientific Process", would you like to learn this? (y/n) -> ')
    print step
if step == 'y':
    os.system('clear')
    print 'The main purpose of scientists is to EXPLAIN everything in our universe.'
    print 'They OBSERVE something that they do not understand. With help from their current knowledge and a bit of research, they form something called a HYPOTHESIS.'
    hypothesis = raw_input('Do you know what a hypothesis is? (y/n) -> ')
    while hypothesis != 'y' and hypothesis != 'n':
        print ' y / n '
        hypothesis = raw_input('Do you know what a hypothesis is? (y/n) -> ')
    if hypothesis == 'y':
        os.system('clear')
    if hypothesis == 'n':
        os.system('clear')
        print 'A hypothesis is a proposed explanation of something that you do not have enough evidence to prove, however, enough to start an investigation'
        print 'Please do not confuse a hypothesis with a theory, a theory is a hypothesis that has already been proven and has all the necessary evidence to back it up.'
        print
        print
    os.system('clear')
    print 'Let\'s carry on shall we?'
    print
    print
    print 'After they have created a hypothesis, they will then TEST this hypothesis to gather data and evidence that support or oppose their hypothesis.'
    print 'These tests are normally carried out through EXPERIMENTS.'
    experiment = raw_input('Do you know what an experiment is? (y/n) -> ')
    while experiment != 'y' and experiment != 'n':
        print ' y / n '
        experiment = raw_input('Do you know what an experiment is? (y/n) -> ')
    if experiment == 'y':
        os.system('clear')
    if experiment == 'n':
        os.system('clear')
        print 'An experiment\'s sole purpose is to produce data that either supports or opposes a set hypothesis.'
        print 'Experiments are normally carried out with extreme organisation and is very detailed, capturing every aspect that may influence the hypothesis.'
        print
        print
    print 'Let\'s carry on.'
    print
    print
    print 'After the experiment has gathered data, the hypothesis either moves towards being true or being rejected.'
    print 'If there is positive evidence found, the hypothesis creates more attention, but is not considered true just yet.'
    print
    print
    print 'That is the simple version of how scientists create and test hypothesis.'
    print
    print
    print 'Scientists normally work in teams.'
    print 'This is to ensure that the same data is observed in multiple ways and interpreted differently.'
    print 'The team then comes up and tests a hypothesis, which they then present to the scientific community through different mediums for the hypothesis to be judged. This is a process called PEER REVIEW.'
    peer_review = raw_input('Do you know what peer review is? (y/n) -> ')
    while peer_review != 'y' and peer_review != 'n':
        print ' y / n '
        peer_review = raw_input('Do you know what peer review is? (y/n) -> ')
    if peer_review == 'y':
        os.system('clear')
    if peer_review == 'n':
        os.system('clear')
        print 'Peer review is simply the process of professionals working in the same field judging and analysing a given work by other professionals.'
        print 'They do this by trying to replicate the data being analysed by using their own means. They try to collect more evidence to either support or oppose the work.'
        print 'After experiments has taken place all over the world and everybody was able to replicate the data and starts to accept it, the hypothesis brought forward by the original team will then upgrade its status into a THEORY, which, as we have learned earlier, is a hypothesis that has been proven.'
        print 'If otherwise, the scientists cannot replicate the data, they then dismiss this hypothesis and try to come up with their own hypothesis or just modify the original hypothesis by adding or removing certain parts.'
        print 'Then the whole process repeats itself.'
        print
        print
    print 'Forward we shall go.'
    print
    print
    print 'After the tedious work of creating a hypothesis, testing it, getting it accepted by the community, and making it a theory, we have to understand that all explanations are provisional, meaning they only explain data with the evidence currently available, further evidence might come up to reinforce or dismiss this explanation.'
    print 'When new evidence do come up, the original hypothesis is analysed all over again and is proven, or not, using the new evidence.'
    print 'But fear not, when a hypothesis or a theory is under the knife because of new evidence found, this is all done to enhance our understanding of science.'
    print 'So be happy if something new comes up, all scientists\' work are just there to uncover the truth about our universe.'
    print
    print
    print 'It all sounds dandy that we are developing so much, however these developments do raise ISSUES.'
    issues = raw_input('Do you know about these issues? (y/n) -> ')
    while issues != 'y' and issues != 'n':
        print ' y / n '
        issues = raw_input('Do you know about these issues? (y/n) -> ')
    if issues == 'y':
        os.system('clear')
    if issues == 'n':
        os.system('clear')
        print 'There are four main issues that rise up as experiments take place.'
        print 'These are: '
        print 'Economic Issues'
        print 'We have to think about the monetary setback that these experiments will produce for the society. Always remember, as more money is used for experiments, less money goes elsewhere.'
        print '--------------'
        print 'Social Issues'
        print 'In a nutshell, social issues are issues that are affecting people, since we normally carry out experiments to help other people, we have to think about others as we make decisions based on scientific evidence.'
        print '--------------'
        print 'Environmental Issues'
        print 'When creating new technology, we have to look at the impact it has on our environment, for example, nuclear power is great and all, however the waste that it produce can have a negative impact on our environment.'
        print '--------------'
        print 'Ethical Issues'
        print 'These issues are raised when we have to think twice whether we should do something based on scientific development. Should we clone humans? Is it really a good idea to develop better nuclear weapons?.'
        print
        print
        print 'Aaaannnnddddd, that\'s it for "The Scientific Process". We hope you enjoyed that chapter.'
        test = raw_input('Would you like to take a test? (y/n) -> ')
        while test != 'y' and test != 'n':
            print ' y / n '
            test = raw_input('Would you like to take a test? (y/n) -> ')
        if test == 'y':
            score = 0
            os.system('clear')
            print 'Okay, let\'s start shall we?'
            print
            q1_hypothesis = raw_input('A hypothesis is something that has been proven and is accepted everywhere - true or false -> ')
            while q1_hypothesis != 'true' and q1_hypothesis != 'false':
                print 'true or false'
                q1_hypothesis = raw_input('A hypothesis is something that has been proven and is accepted everywhere - true or false -> ')
            if q1_hypothesis == 'true':
                print
                print 'Not quite.'
            if q1_hypothesis == 'false':
                print
                print 'That is right,'
                score = score + 1
            print
            print 'a hypothesis is something that has been observed and needs more evidence to be either proven right or wrong.'
            print 'It\'s presented to the scientific community and is judged and replicated before it is either dismissed due to lack of evidence or accepted and turned into a theory.'
            print
            print
            print 'Next question!'
            print
            q2_peer_review = raw_input('Peer review is when professionals in the field try to replicate data by doing their own experiments and ultimately approve, or dismiss a hypothesis. - true or false -> ')
            while q2_peer_review != 'true' and q2_peer_review != 'false':
                print 'true or false'
                q2_peer_review = raw_input('Peer review is when professionals in the field try to replicate data by doing their own experiments and ultimately approve, or dismiss a hypothesis. - true or false -> ')
            if q2_peer_review == 'true':
                print
                print 'Correct.'
                score = score + 1
            if q2_peer_review == 'false':
                print
                print 'Nope.'
            print
            print 'Peer review is the process of professionals working in the same field judging and analysing a given work by other professionals.'
            print
            print 'Almost there!'
            print
            q3_social_issues = raw_input('Social issues based on scientific development are issues that arise when Facebook servers go down - true or false -> ')
            while q3_social_issues != 'true' and q3_social_issues != 'false':
                print 'true or false'
                q3_social_issues = raw_input('Social issues based on scientific development are issues that arise when Facebook servers go down - true or false -> ')
            if q3_social_issues == 'true':
                print
                print 'It may seem like an issue, but not really. Just, just no.'
            if q3_social_issues == 'false':
                print
                print 'At least someone\'s paying attention!'
                score = score + 1
            print
            print 'Do remember, that social issues that are raised from scientific development are decisions that are made based on scientific evidence that can affect humans.'
            print
            print 'That\'s it for the questions!'
            if score == 1:
                print 'You scored 1 out of 3, guess you have to go through this chapter again, please do try again.'
                print 'Try your best and you will get there, I promise you.'
            if score == 2:
                print 'You scored 2 out of 3, it\'s not perfect, but at least it shows you are progressing. Try to repeat the chapter again and see if you can understand it some more.'
                print 'Well done to you, please learn some more.'
            if score == 3:
                print 'Look at you, scoring 3 out of 3. It\'s a good start, try to go through the chapter again and just revise what you have learned.'
                print 'Congratulations.'
            print
            print 'Well that\'s it for this chapter, we hope that you have learned as much as you can. Please try to go through it again and revise what you have learned.'
            print 'Try to teach someone else what you have learned. It is the best way to learn a new subject.'
            print 'Goodbye for now.'
            confirm = raw_input('Enter "exit" to leave this chapter -> ')
            while confirm != 'exit':
                print 'Go on, enter "exit"'
                print
                confirm = raw_input('Enter "exit" to leave this chapter -> ')
os.system('clear')
print 'Thank you for using this GCSE Physics helper program. Please try our other programs to help you ace all of those exams!'
print 'Goodbye!'
exit

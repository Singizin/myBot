      program main
      common /sizes/ n, k, l
      dimension arr(1000000)
      
      call read_sizes
      call read_data(arr, arr(n*(k+1)+1))
      
      call multiply(arr, arr(n*(k+1)+1), arr(n*(k+1)+n+1))
      
      write (*,*) 'Done'
      pause
      end
      
      subroutine read_sizes
      common /sizes/ n, k, l
      open(1, file = 'sizes.txt') 
      read(1,*) n, k, l
      
      if (n.NE.l) then
      print *, 'multiplying is impossible'
      pause
      stop
      end if
      end

      subroutine read_data(arr, vector)
      common /sizes/ n, k, l
      dimension arr(n, k + 1)
      dimension vector(l)
      
      open(1, file = 'matrix.txt')
      open(2, file = 'vector.txt')
      
      read(1,*) ((arr(i,j), j=1,k+1), i=1,n)
      read(2,*) (vector(i), i=1,n)
      
 100  format(F5.1, ' ' \)
 101  format(I4)
      
      do i=1, n
        do j=1, k+1
        write(*,100) arr(i,j)
        end do
        write(*,101)
      end do
      
      do i=1, n
        write(*,100) vector(i)
        write(*,101)
      end do
      end
      
      subroutine multiply(a, b, v)
      common /sizes/ n, k, l
      dimension a(n, k + 1)
      dimension b(l)
      dimension v(l)
      integer start
      
      write(*,101)
      do i=1, n
        write(*,100) v(i)
        write(*,101)
      end do
      write(*,101)
      
      start = k + 1
      index = 1
      do i=1, k+1
        iindex = 1
        do j=start, k+1
          v(i) = v(i) + a(i,j)*b(iindex)
          iindex=iindex+1
        end do
        start=start-1
      end do
      
      do i=1, n
        write(*,100) v(i)
        write(*,101)
      end do
      write(*,101)
        
      index=index+1
      do i=k+2, n
        iindex = index
        do j=1, k+1
          v(i) = v(i) + a(i,j)*b(iindex)
          iindex=iindex+1
        end do
        index=index+1
      end do
      
      do i=1, n
        write(*,100) v(i)
        write(*,101)
      end do
      write(*,101)
        
      do i=1, n-k
        iindex=i+1
        do j=1, k
          v(i) = v(i) + a(i+j,k+1-j)*b(iindex)
          iindex=iindex+1
        end do
      end do   
      
      do i=1, n
        write(*,100) v(i)
        write(*,101)
      end do
      write(*,101)

      do i=n-k+1, n-1
        iindex = i + 1
        do j=1, n-i
          v(i) = v(i) + a(i+j,k+1-j)*b(iindex)
          iindex=iindex+1
        end do
      end do
      
      do i=1, n
        write(*,100) v(i)
        write(*,101)
      end do
      write(*,101)
      
 100  format(F5.1, ' ' \)
 101  format(I4)
        
      end


